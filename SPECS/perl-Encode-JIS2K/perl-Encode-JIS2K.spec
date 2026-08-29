# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Encode-JIS2K
Version:        0.05
Release:        %autorelease
Summary:        JIS X 0212 (aka JIS 2000) Encodings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Encode-JIS2K
#!RemoteAsset:  sha256:022f1f3d6869742b3718c27bfcca6f7c96aceffac0a2267d140bbf653d7c0ac2
Source0:        https://www.cpan.org/authors/id/D/DA/DANKOGAI/Encode-JIS2K-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl-devel
BuildRequires:  perl(Encode) >= 1.41
BuildRequires:  perl(ExtUtils::MakeMaker)

Requires:       perl(Encode) >= 1.41

%description
To find out how to use this module in detail, see Encode.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
