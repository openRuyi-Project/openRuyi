# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Data-Compare
Version:        1.29
Release:        %autorelease
Summary:        Compare perl data structures
License:        GPL-2.0-only OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Data-Compare
#!RemoteAsset:  sha256:53c9db3b93263c88aaa3c4072d819eaded024d7a36b38c0c37737d288d5afa8c
Source0:        https://www.cpan.org/authors/id/D/DC/DCANTRELL/Data-Compare-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Clone) >= 0.43
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find::Rule) >= 0.1
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Number::Compare)

Requires:       perl(Clone) >= 0.43
Requires:       perl(File::Find::Rule) >= 0.1
Requires:       perl(Test::More) >= 0.88

%description
Compare two perl data structures recursively. Returns 0 if the structures
differ, else returns 1.

%files -f %{name}.files
%doc CHANGELOG MAINTAINERS-NOTE NOTES README

%changelog
%autochangelog
