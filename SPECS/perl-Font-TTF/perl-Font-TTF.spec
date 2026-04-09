# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Font-TTF
Version:        1.06
Release:        %autorelease
Summary:        Perl module for TrueType Font hacking
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Font-TTF
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/B/BH/BHALLISSY/Font-TTF-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
This module allows you to do almost anything to a TrueType/OpenType Font
including modify and inspect nearly all tables.

%prep
%setup -q -n Font-TTF-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTORS README.TXT TODO

%changelog
%autochangelog
