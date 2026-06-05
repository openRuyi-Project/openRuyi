# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Exporter-Tiny
Version:        1.006003
Release:        %autorelease
Summary:        Exporter with the features of Sub::Exporter but only core dependencies
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Exporter-Tiny
#!RemoteAsset:  sha256:6499f09a6432cf87b133fb9580a8a9a9a6c566821346b1fdee95f7b64c0317b1
Source0:        https://www.cpan.org/authors/id/T/TO/TOBYINK/Exporter-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.1
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.47

%description
Exporter::Tiny supports many of Sub::Exporter's external-facing features
including renaming imported functions with the -as, -prefix and -suffix
options; explicit destinations with the into option; and alternative
installers with the installer option. But it's written in only about 40% as
many lines of code and with zero non-core dependencies.

%files -f %{name}.files
%doc Changes CREDITS doap.ttl NEWS README TODO

%changelog
%autochangelog
