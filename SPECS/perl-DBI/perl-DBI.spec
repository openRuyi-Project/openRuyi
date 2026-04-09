# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-DBI
Version:        1.647
Release:        %autorelease
Summary:        Database independent interface for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/DBI
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/H/HM/HMBRAND/DBI-%{version}.tgz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Simple) >= 0.90

%description
The DBI is a database access module for the Perl programming language.
It defines a set of methods, variables, and conventions that provide a
consistent database interface, independent of the actual database
being used.

%prep
%setup -q -n DBI-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ChangeLog Driver.xst README.md

%changelog
%autochangelog
