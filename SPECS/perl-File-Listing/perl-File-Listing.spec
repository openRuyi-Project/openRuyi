# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-File-Listing
Version:        6.16
Release:        %autorelease
Summary:        Parse directory listing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/File-Listing
#!RemoteAsset:  sha256:189b3a13fc0a1ba412b9d9ec5901e9e5e444cc746b9f0156d4399370d33655c6
Source0:        https://www.cpan.org/authors/id/P/PL/PLICEASE/File-Listing-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(Test::More) >= 0.98

Requires:       perl(Exporter) >= 5.57

%description
This module exports a single function called parse_dir, which can be used
to parse directory listings.

%files -f %{name}.files
%doc author.yml Changes Changes.original perlcriticrc README

%changelog
%autochangelog
