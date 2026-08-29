# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-List-MoreUtils-XS
Version:        0.430
Release:        %autorelease
Summary:        Provide compiled List::MoreUtils functions
License:        Apache-2.0
URL:            https://metacpan.org/dist/List-MoreUtils-XS
#!RemoteAsset:  sha256:e8ce46d57c179eecd8758293e9400ff300aaf20fefe0a9d15b9fe2302b9cb242
Source0:        https://www.cpan.org/authors/id/R/RE/REHSACK/List-MoreUtils-XS-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(XSLoader) >= 0.22

Requires:       perl(XSLoader) >= 0.22

%description
List::MoreUtils::XS is a backend for List::MoreUtils. Even if it's possible
(because of user wishes) to have it practically independent from
List::MoreUtils, it technically depend on List::MoreUtils. Since it's only
a backend, the API is not public and can change without any warning.

%files -f %{name}.files
%doc ARTISTIC-1.0 Changes GPL-1 MAINTAINER.md README.md

%changelog
%autochangelog
