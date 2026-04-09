# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-DBD-CSV
Version:        0.62
Release:        %autorelease
Summary:        DBI driver for CSV files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/DBD-CSV
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/H/HM/HMBRAND/DBD-CSV-%{version}.tgz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(charnames)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DBD::File) >= 0.42
BuildRequires:  perl(DBI) >= 1.628
BuildRequires:  perl(Encode) >= 3.12
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(SQL::Statement) >= 1.405
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More) >= 0.90
BuildRequires:  perl(Text::CSV_XS) >= 1.01

Requires:       perl(DBD::File) >= 0.42
Requires:       perl(DBI) >= 1.628
Requires:       perl(Encode) >= 3.12
Requires:       perl(SQL::Statement) >= 1.405
Requires:       perl(Test::More) >= 0.90
Requires:       perl(Text::CSV_XS) >= 1.01

%description
The DBD::CSV module is yet another driver for the DBI (Database independent
interface for Perl). This one is based on the SQL "engine" SQL::Statement
and the abstract DBI driver DBD::File and implements access to so-called
CSV files (Comma Separated Values). Such files are often used for exporting
MS Access and MS Excel data.

%prep
%setup -q -n DBD-CSV-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ChangeLog CONTRIBUTING.md README SECURITY.md

%changelog
%autochangelog
