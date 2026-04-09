# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-String-Format
Version:        1.18
Release:        %autorelease
Summary:        Sprintf-like string formatting capabilities with arbitrary format definitions
License:        GPL-2.0-only
URL:            https://metacpan.org/dist/String-Format
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/S/SR/SREZIC/String-Format-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

%description
String::Format lets you define arbitrary printf-like format sequences to be
expanded. This module would be most useful in configuration files and
reporting tools, where the results of a query need to be formatted in a
particular way. It was inspired by mutt's index_format and related
directives (see <URL:http://www.mutt.org/doc/manual/manual-
6.html#index_format>).

%prep
%setup -q -n String-Format-%{version}

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
