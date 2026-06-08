# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Scalar-List-Utils
Version:        1.70
Release:        %autorelease
Summary:        Distribution of general-utility subroutines
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Scalar-List-Utils
#!RemoteAsset:  sha256:e0cc03f9fe3565cdf4d6102654f87bba3bca2d8ff989da38307e857d0ae3c886
Source0:        https://www.cpan.org/authors/id/P/PE/PEVANS/Scalar-List-Utils-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

%description
Scalar::List::Utils does nothing on its own. It is packaged with several
useful modules.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
