%define	module	Pod-Escapes
%define	name	perl-%{module}
%define version 1.04
%define release %mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl module to resolve Pod E<...> sequences
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/S/SB/SBURKE/%{module}-%{version}.tar.gz
Url:            http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Pod::Simple is a module to resolve Pod E<...> sequences.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorlib}/Pod
%{_mandir}/man3/*

