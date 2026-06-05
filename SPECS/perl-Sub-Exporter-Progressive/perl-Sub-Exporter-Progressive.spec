# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Sub-Exporter-Progressive
Version:        0.001013
Release:        %autorelease
Summary:        Only use Sub::Exporter if you need it
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Sub-Exporter-Progressive
#!RemoteAsset:  sha256:d535b7954d64da1ac1305b1fadf98202769e3599376854b2ced90c382beac056
Source0:        https://www.cpan.org/authors/id/F/FR/FREW/Sub-Exporter-Progressive-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.88

%description
Sub::Exporter is an incredibly powerful module, but with that power comes
great responsibility, er- as well as some runtime penalties. This module is
a Sub::Exporter wrapper that will let your users just use Exporter if all
they are doing is picking exports, but use Sub::Exporter if your users try
to use Sub::Exporter's more advanced features, like renaming exports, if
they try to use them.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
