# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Task-Weaken
Version:        1.06
Release:        %autorelease
Summary:        Ensure that a platform has weaken support
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Task-Weaken
#!RemoteAsset:  sha256:2383fedb9dbaef646468ea824afbf7c801076720cfba0df2a7a074726dcd66be
Source0:        https://www.cpan.org/authors/id/E/ET/ETHER/Task-Weaken-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Scalar::Util) >= 1.14
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
One recurring problem in modules that use Scalar::Util's weaken function is
that it is not present in the pure-perl variant.

%files -f %{name}.files
%doc Changes CONTRIBUTING Makefile.footer Makefile.header README

%changelog
%autochangelog
