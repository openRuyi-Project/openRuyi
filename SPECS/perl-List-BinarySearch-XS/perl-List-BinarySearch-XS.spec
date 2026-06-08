# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-List-BinarySearch-XS
Version:        0.09
Release:        %autorelease
Summary:        Binary Search a sorted array with XS routines
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/List-BinarySearch-XS
#!RemoteAsset:  sha256:9ceb9fc3c1fc3418eb8d372be03d566a35dde6df06d55a6096a305891581f4c2
Source0:        https://www.cpan.org/authors/id/D/DA/DAVIDO/List-BinarySearch-XS-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.98

%description
A binary search searches sorted lists using a divide and conquer technique.
On each iteration the search domain is cut in half, until the result is
found. The computational complexity of a binary search is O(log n).

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
