# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-MIME-Base32
Version:        1.303
Release:        %autorelease
Summary:        Base32 encoder and decoder
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/MIME-Base32
#!RemoteAsset:  sha256:ab21fa99130e33a0aff6cdb596f647e5e565d207d634ba2ef06bdbef50424e99
Source0:        https://www.cpan.org/authors/id/R/RE/REHSACK/MIME-Base32-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.9
BuildRequires:  perl(utf8)

%description
This module is for encoding/decoding data much the way that
MIME::Base64 does.

%files -f %{name}.files
%doc ARTISTIC-1.0 Changes GPL-1 README.md

%changelog
%autochangelog
