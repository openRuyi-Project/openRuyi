# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Jcode
Version:        2.07
Release:        %autorelease
Summary:        Japanese Charset Handler
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Jcode
#!RemoteAsset:  sha256:ed1ce473ec869089e52016cfc8355165ebc37be9694ba4e829c7eb4ba1c45f8d
Source0:        https://www.cpan.org/authors/id/D/DA/DANKOGAI/Jcode-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MIME::Base64) >= 2.1

Requires:       perl(MIME::Base64) >= 2.1

%description
<Japanese document is now available as Jcode::Nihongo. >

%files -f %{name}.files
%doc Changes Changes.ver0X README

%changelog
%autochangelog
