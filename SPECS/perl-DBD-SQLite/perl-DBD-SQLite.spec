# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-DBD-SQLite
Version:        1.78
Release:        %autorelease
Summary:        Self-contained RDBMS in a DBI Driver
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/DBD-SQLite
#!RemoteAsset:  sha256:efbad7794bafaa4e7476c07445a33bbfe1040e380baa3395a02635eebe3859d5
Source0:        https://www.cpan.org/authors/id/I/IS/ISHIGAKI/DBD-SQLite-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(DBI) >= 1.57
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec) >= 0.82
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl-devel

Requires:       perl(DBI) >= 1.57

%description
SQLite is a public domain file-based relational database engine that you
can find at https://www.sqlite.org/.

%files -f %{name}.files
%doc Changes constants.inc dbdimp_tokenizer.inc dbdimp_virtual_table.inc README

%changelog
%autochangelog
