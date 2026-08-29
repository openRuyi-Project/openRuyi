# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-AnyEvent-I3
Version:        0.19
Release:        %autorelease
Summary:        Communicate with the i3 window manager
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/AnyEvent-I3
#!RemoteAsset:  sha256:1bcd3b60db3d5560148de791353e8af1172264f5a85e77197b9ffc041dac483a
Source0:        https://www.cpan.org/authors/id/M/MS/MSTPLBG/AnyEvent-I3-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl-devel
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(AnyEvent::Handle)
BuildRequires:  perl(AnyEvent::Socket)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Types::Serialiser)
BuildRequires:  perl(common::sense)

Requires:       perl(AnyEvent)
Requires:       perl(JSON::XS)
Requires:       perl(Types::Serialiser)
Requires:       perl(common::sense)

%description
AnyEvent::I3 connects to the i3 window manager through its UNIX socket based
IPC interface.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
