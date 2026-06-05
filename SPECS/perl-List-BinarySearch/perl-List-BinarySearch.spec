# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-List-BinarySearch
Version:        0.25
Release:        %autorelease
Summary:        Binary Search within a sorted array
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/List-BinarySearch
#!RemoteAsset:  sha256:c8113071bd6040035ee8ab01cf1b72a910574192f1d179102ae775a973f2e82a
Source0:        https://www.cpan.org/authors/id/D/DA/DAVIDO/List-BinarySearch-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::BinarySearch::XS) >= 0.06
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.98

Requires:       perl(List::BinarySearch::XS) >= 0.06

%description
A binary search searches sorted lists using a divide and conquer technique.
On each iteration the search domain is cut in half, until the result is
found. The computational complexity of a binary search is O(log n).

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
