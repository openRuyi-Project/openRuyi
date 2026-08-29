# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Ref-Util
Version:        0.204
Release:        %autorelease
Summary:        Utility functions for checking references
License:        MIT
URL:            https://metacpan.org/dist/Ref-Util
#!RemoteAsset:  sha256:415fa73dbacf44f3d5d79c14888cc994562720ab468e6f71f91cd1f769f105e1
Source0:        https://www.cpan.org/authors/id/A/AR/ARC/Ref-Util-%{version}.tar.gz
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
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.96

Requires:       perl(Exporter) >= 5.57

%description
Ref::Util introduces several functions to help identify references in a
smarter (and usually faster) way. In short:

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
