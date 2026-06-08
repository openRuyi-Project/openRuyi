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
#!RemoteAsset:  sha256:4b697d444259759ea02d2c442c9bffe5ffe14c9214084a01f743693a944cc293
Source0:        https://www.cpan.org/authors/id/B/BH/BHALLISSY/Font-TTF-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::String)

%description
This module allows you to do almost anything to a TrueType/OpenType Font
including modify and inspect nearly all tables.

%files -f %{name}.files
%doc Changes CONTRIBUTORS README.TXT TODO

%changelog
%autochangelog
