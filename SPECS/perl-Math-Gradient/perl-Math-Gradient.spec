# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Math-Gradient
Version:        0.04
Release:        %autorelease
Summary:        Perl extension for calculating gradients for colour transitions, etc
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Math-Gradient
#!RemoteAsset:  sha256:0b8fb5b3be303ee22b582f7b97edf7ed79799d7a473649ef12a14a1796d47d2d
Source0:        https://www.cpan.org/authors/id/C/CR/CRAKRJACK/Math-Gradient-%{version}.tgz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
Math::Gradient is used to calculate smooth transitions between numerical
values (also known as a "Gradient"). I wrote this module mainly to mix
colours, but it probably has several other applications. Methods are
supported to handle both basic and multiple-point gradients, both with
scalars and arrays.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
