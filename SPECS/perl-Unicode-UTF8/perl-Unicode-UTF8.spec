# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Unicode-UTF8
Version:        0.70
Release:        %autorelease
Summary:        Encoding and decoding of UTF-8 encoding form
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Unicode-UTF8
#!RemoteAsset:  sha256:4ed46cdd3b6196e3f803ce3d01fa94fba9834ab86a0b1d3978e547fe60cd2e26
Source0:        https://www.cpan.org/authors/id/C/CH/CHANSEN/Unicode-UTF8-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl-devel
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode) >= 1.9801
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Fatal) >= 0.006
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(Devel::AssertC99)

%description
This module provides functions to encode and decode UTF-8 encoding form as
specified by Unicode and ISO/IEC 10646:2011.

%files -f %{name}.files
%doc Changes prereqs.yml README

%changelog
%autochangelog
