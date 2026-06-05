# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Digest-Perl-MD5
Version:        1.91
Release:        %autorelease
Summary:        Digest::Perl::MD5 Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Digest-Perl-MD5
#!RemoteAsset:  sha256:718e41717fb82a9ab3f0809d211fddcdbdef91dc198887d82b88723aa54afcd5
Source0:        https://www.cpan.org/authors/id/D/DE/DELTA/Digest-Perl-MD5-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
This module has the same interface as the much faster Digest::MD5. So you
can easily exchange them, e.g.

%files -f %{name}.files
%doc CHANGES rand.f README.md

%changelog
%autochangelog
