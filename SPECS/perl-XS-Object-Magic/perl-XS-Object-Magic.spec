# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-XS-Object-Magic
Version:        0.05
Release:        %autorelease
Summary:        Opaque extensible XS pointer-backed objects
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/XS-Object-Magic
#!RemoteAsset:  sha256:3dc9e460cee92e11744062754643a33778ca52a54d205fcaffa4ab0f3cf15e5a
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/XS-Object-Magic-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl-devel
BuildRequires:  perl(ExtUtils::Depends) >= 0.302
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)

%description
XS::Object::Magic provides a small XS helper for opaque pointer-backed objects
using Perl magic.

%files -f %{name}.files
%doc Changes CONTRIBUTING INSTALL README
%license LICENCE

%changelog
%autochangelog
