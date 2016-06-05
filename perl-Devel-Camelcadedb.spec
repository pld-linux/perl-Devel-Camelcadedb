#
# Conditional build:
%bcond_with	tests		# do not perform "make test"

%define		pdir	Devel
%define		pnam	Camelcadedb
%include	/usr/lib/rpm/macros.perl
Summary:	Devel::Camelcadedb - Perl side of the Perl debugger for IntelliJ IDEA and other JetBrains IDE
Name:		perl-%{pdir}-%{pnam}
Version:	1.6.1.2
Release:	1
License:	MIT
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	aaca6cca7ebee67c9707ee76e35f74a5
URL:		http://search.cpan.org/dist/Devel-Camelcadedb/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(JSON::XS) >= 3.02
BuildRequires:	perl(PadWalker) >= 2.2
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module should be installed for debugging using Camelcade plugin
for IntelliJ IDEA

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Devel/Camelcadedb.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md Changes
%{perl_vendorlib}/Devel/Camelcadedb.pm
%{_mandir}/man3/Devel::Camelcadedb.3pm*
