# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Encode-HanExtra
Version:        0.23
Release:        %autorelease
Summary:        Extra sets of Chinese encodings
License:        MIT
URL:            https://metacpan.org/dist/Encode-HanExtra
#!RemoteAsset:  sha256:1fd4b06cada70858003af153f94c863b3b95f2e3d03ba18d0451a81d51db443a
Source0:        https://www.cpan.org/authors/id/A/AU/AUDREYT/Encode-HanExtra-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.7.3
BuildRequires:  perl(Encode) >= 1.41
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(inc::Module::Install)

Requires:       perl(Encode) >= 1.41

%description
Perl 5.7.3 and later ships with an adequate set of Chinese encodings,
including the commonly used CP950, CP936 (also known as GBK), Big5 (alias
for Big5-Eten), Big5-HKSCS, EUC-CN, HZ, and ISO-IR-165.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
