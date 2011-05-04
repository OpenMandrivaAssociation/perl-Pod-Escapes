%define	upstream_name	 Pod-Escapes
%define upstream_version 1.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Perl module to resolve Pod E<...> sequences
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/S/SB/SBURKE/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Pod::Simple is a module to resolve Pod E<...> sequences.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
