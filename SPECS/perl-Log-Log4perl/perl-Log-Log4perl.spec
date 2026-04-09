# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Log-Log4perl
Version:        1.57
Release:        %autorelease
Summary:        Log4j implementation for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Log-Log4perl
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/E/ET/ETJ/Log-Log4perl-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(DBD::CSV) >= 0.33
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI) >= 1.607
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path) >= 2.07
BuildRequires:  perl(File::Spec) >= 0.82
BuildRequires:  perl(Log::Dispatch)
BuildRequires:  perl(Log::Dispatch::FileRotate) >= 1.10
BuildRequires:  perl(SQL::Statement) >= 1.20
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(XML::DOM) >= 1.29

Requires:       perl(DBD::CSV) >= 0.33
Requires:       perl(DBI) >= 1.607
Requires:       perl(File::Path) >= 2.07
Requires:       perl(File::Spec) >= 0.82
Requires:       perl(Log::Dispatch::FileRotate) >= 1.10
Requires:       perl(SQL::Statement) >= 1.20
Requires:       perl(XML::DOM) >= 1.29

%description
Log::Log4perl lets you remote-control and fine-tune the logging behaviour
of your system from the outside. It implements the widely popular (Java-
based) Log4j logging package in pure Perl.

%prep
%setup -q -n Log-Log4perl-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
