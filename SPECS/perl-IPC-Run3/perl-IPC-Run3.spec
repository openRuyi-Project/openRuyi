# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-IPC-Run3
Version:        0.049
Release:        %autorelease
Summary:        Run a subprocess in batch mode
License:        GPL-1.0-or-later OR Artistic-1.0-Perl OR BSD-2-Clause
URL:            https://metacpan.org/dist/IPC-Run3
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/IPC-Run3-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.31
BuildRequires:  perl(Time::HiRes)

Requires:       perl(Test::More) >= 0.31

%description
This module allows you to run a subprocess and redirect stdin, stdout,
and/or stderr to files and perl data structures. It aims to satisfy 99%
of the need for using system, qx, and open3 with a simple, extremely
Perlish API.

%prep
%setup -q -n IPC-Run3-%{version}

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
