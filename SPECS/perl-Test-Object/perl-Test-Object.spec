# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-Object
Version:        0.08
Release:        %autorelease
Summary:        Thoroughly testing objects via registered handlers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Test-Object
#!RemoteAsset:  sha256:65278964147837313f4108e55b59676e8a364d6edf01b3dc198aee894ab1d0bb
Source0:        https://www.cpan.org/authors/id/E/ET/ETHER/Test-Object-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util) >= 1.16
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

Requires:       perl(Scalar::Util) >= 1.16

%description
In situations where you have deep trees of classes, there is a common
situation in which you test a module 4 or 5 subclasses down, which should
follow the correct behaviour of not just the subclass, but of all the
parent classes.

%files -f %{name}.files
%doc Changes CONTRIBUTING README

%changelog
%autochangelog
