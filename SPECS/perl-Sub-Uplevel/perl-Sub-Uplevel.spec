# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Sub-Uplevel
Version:        0.2800
Release:        %autorelease
Summary:        Apparently run a function in a higher stack frame
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Sub-Uplevel
#!RemoteAsset:  sha256:b4f3f63b80f680a421332d8851ddbe5a8e72fcaa74d5d1d98f3c8cc4a3ece293
Source0:        https://www.cpan.org/authors/id/D/DA/DAGOLDEN/Sub-Uplevel-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
Like Tcl's uplevel() function, but not quite so dangerous. The idea is
just to fool caller(). All the really naughty bits of Tcl's uplevel()
are avoided.

%files -f %{name}.files
%doc Changes CONTRIBUTING.mkdn perlcritic.rc README

%changelog
%autochangelog
