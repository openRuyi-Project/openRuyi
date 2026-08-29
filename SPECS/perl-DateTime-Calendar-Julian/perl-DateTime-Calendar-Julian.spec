# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-DateTime-Calendar-Julian
Version:        0.107
Release:        %autorelease
Summary:        Dates in the Julian calendar
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/DateTime-Calendar-Julian
#!RemoteAsset:  sha256:fcb2b424844bb13bcad46b1c7aa239b5a09bab2556f53bd1f27fad90c260d33d
Source0:        https://www.cpan.org/authors/id/W/WY/WYANT/DateTime-Calendar-Julian-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.4
BuildRequires:  perl(Clone)
BuildRequires:  perl(DateTime) >= 1.48
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Eval::Closure)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

Requires:       perl(DateTime) >= 1.48

%description
DateTime::Calendar::Julian implements the Julian Calendar. This module
implements all methods of DateTime; see the DateTime(3) manpage for
all methods.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
