# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Crypt-RC4
Version:        2.02
Release:        %autorelease
Summary:        Perl implementation of the RC4 encryption algorithm
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Crypt-RC4
#!RemoteAsset:  sha256:5ec4425c6bc22207889630be7350d99686e62a44c6136960110203cd594ae0ea
Source0:        https://www.cpan.org/authors/id/S/SI/SIFUKURT/Crypt-RC4-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
A simple implementation of the RC4 algorithm, developed by RSA Security,
Inc. Here is the description from RSA's website:

%files -f %{name}.files
%doc Changes

%changelog
%autochangelog
