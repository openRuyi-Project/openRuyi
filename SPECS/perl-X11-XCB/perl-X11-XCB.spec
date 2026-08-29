# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-X11-XCB
Version:        0.25
Release:        %autorelease
Summary:        Perl bindings for libxcb
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/X11-XCB
#!RemoteAsset:  sha256:094dd60e7c0040958f320c9bb22eb88e488a29914fea30a7d30998ec23be447b
Source0:        https://cpan.metacpan.org/authors/id/Z/ZH/ZHMYLOVE/X11-XCB-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl-devel
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Devel::PPPort) >= 3.19
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.18
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(XML::Descent)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(XS::Object::Magic)
BuildRequires:  pkgconfig(xcb) >= 1.2
BuildRequires:  xcb-proto
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xinerama)
BuildRequires:  pkgconfig(xcb-xkb)

Requires:       perl(Data::Dump)
Requires:       perl(Mouse)
Requires:       perl(Try::Tiny)
Requires:       perl(XML::Descent)
Requires:       perl(XML::Simple)
Requires:       perl(XS::Object::Magic)

%description
X11::XCB provides Perl bindings for libxcb and selected XCB extension helper
libraries.

%files -f %{name}.files
%doc Changes INSTALL.md README.md

%changelog
%autochangelog
