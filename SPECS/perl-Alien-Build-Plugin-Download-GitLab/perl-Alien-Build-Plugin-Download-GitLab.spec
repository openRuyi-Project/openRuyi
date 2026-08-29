# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Alien-Build-Plugin-Download-GitLab
Version:        0.01
Release:        %autorelease
Summary:        Alien::Build plugin to download from GitLab
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Alien-Build-Plugin-Download-GitLab
#!RemoteAsset:  sha256:c1f089c8ea152a789909d48a83dbfcf2626f773daf30431c8622582b26aba902
Source0:        https://www.cpan.org/authors/id/P/PL/PLICEASE/Alien-Build-Plugin-Download-GitLab-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.4
BuildRequires:  perl(Alien::Build::Plugin)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test2::V0) >= 0.000121
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)

%description
This plugin is designed for downloading assets from a GitLab instance.

%files -f %{name}.files
%doc author.yml Changes perlcriticrc README

%changelog
%autochangelog
