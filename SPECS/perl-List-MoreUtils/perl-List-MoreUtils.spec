# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-List-MoreUtils
Version:        0.430
Release:        %autorelease
Summary:        Provide the stuff missing in List::Util
License:        Apache-2.0
URL:            https://metacpan.org/dist/List-MoreUtils
#!RemoteAsset:  sha256:63b1f7842cd42d9b538d1e34e0330de5ff1559e4c2737342506418276f646527
Source0:        https://www.cpan.org/authors/id/R/RE/REHSACK/List-MoreUtils-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(Exporter::Tiny) >= 0.038
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::MoreUtils::XS) >= 0.430
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl-devel

Requires:       perl(Exporter::Tiny) >= 0.038
Requires:       perl(List::MoreUtils::XS) >= 0.430

%description
List::MoreUtils provides some trivial but commonly needed functionality on
lists which is not going to go into List::Util.

%files -f %{name}.files
%doc ARTISTIC-1.0 Changes GPL-1 README.md

%changelog
%autochangelog
