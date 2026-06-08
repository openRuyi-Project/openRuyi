# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Class-XSAccessor
Version:        1.19
Release:        %autorelease
Summary:        Generate fast XS accessors without runtime compilation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Class-XSAccessor
#!RemoteAsset:  sha256:99c56b395f1239af19901f2feeb125d9ecb4e351a0d80daa9529211a4700a6f2
Source0:        https://www.cpan.org/authors/id/S/SM/SMUELLER/Class-XSAccessor-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(XSLoader)

%description
Class::XSAccessor implements fast read, write and read/write accessors in
XS. Additionally, it can provide predicates such as has_foo() for testing
whether the attribute foo exists in the object (which is different from "is
defined within the object"). It only works with objects that are
implemented as ordinary hashes. Class::XSAccessor::Array implements the
same interface for objects that use arrays for their internal
representation.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
