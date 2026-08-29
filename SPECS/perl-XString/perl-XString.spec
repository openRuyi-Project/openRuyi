# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-XString
Version:        0.005
Release:        %autorelease
Summary:        Isolated String helpers from B
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/XString
#!RemoteAsset:  sha256:f247f55c19aee6ba4a1ae73c0804259452e02ea85a9be07f8acf700a5138f884
Source0:        https://www.cpan.org/authors/id/A/AT/ATOOMIC/XString-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.87
BuildRequires:  perl-devel

%description
XString provides the B string helpers in one isolated package. Right now
only cstring and perlstring are available.

%files -f %{name}.files
%doc Changes README tidyall.ini weaver.ini

%changelog
%autochangelog
