# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-ExtUtils-ParseXS
Version:        3.60
Release:        %autorelease
Summary:        Converts Perl XS code into C code
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/ExtUtils-ParseXS
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/L/LE/LEONT/ExtUtils-ParseXS-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.46
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More) >= 0.47

Requires:       perl(Exporter) >= 5.57
Requires:       perl(ExtUtils::MakeMaker) >= 6.46
Requires:       perl(Test::More) >= 0.47

%description
ExtUtils::ParseXS will compile XS code into C code by embedding the
constructs necessary to let C functions manipulate Perl values and creates
the glue necessary to let Perl access those functions. The compiler uses
typemaps to determine how to map C function parameters and variables to
Perl values.

%prep
%setup -q -n ExtUtils-ParseXS-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
