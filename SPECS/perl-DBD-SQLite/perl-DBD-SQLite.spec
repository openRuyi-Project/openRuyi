# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-DBD-SQLite
Version:        1.76
Release:        %autorelease
Summary:        Self-contained RDBMS in a DBI Driver
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/DBD-SQLite
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/I/IS/ISHIGAKI/DBD-SQLite-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(DBI) >= 1.57
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec) >= 0.82
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Tie::Hash)

Requires:       perl(DBI) >= 1.57

%description
SQLite is a public domain file-based relational database engine that you
can find at https://www.sqlite.org/.

%prep
%setup -q -n DBD-SQLite-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes constants.inc dbdimp_tokenizer.inc dbdimp_virtual_table.inc README

%changelog
%autochangelog
