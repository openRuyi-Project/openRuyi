# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Encode-EUCJPASCII
Version:        0.03
Release:        %autorelease
Summary:        EucJP-ascii - An eucJP-open mapping
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Encode-EUCJPASCII
#!RemoteAsset:  sha256:f998d34d55fd9c82cf910786a0448d1edfa60bf68e2c2306724ca67c629de861
Source0:        https://www.cpan.org/authors/id/N/NE/NEZUMI/Encode-EUCJPASCII-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(Encode) >= 1.41
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

Requires:       perl(Encode) >= 1.41

%description
This module provides eucJP-ascii, one of eucJP-open mappings, and its
derivative. Following encodings are supported.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
