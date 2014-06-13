%define	modname	Pod-Escapes
%define modver	1.04

Summary:	Perl module to resolve Pod E<...> sequences
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	11
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/S/SB/SBURKE/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Pod::Simple is a module to resolve Pod E<...> sequences.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
make test

%files
%doc ChangeLog README
%{perl_vendorlib}/Pod
%{_mandir}/man3/*

