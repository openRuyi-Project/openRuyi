# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Data-Uniqid
Version:        0.12
Release:        %autorelease
Summary:        Perl extension for simple genrating of unique id's
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Data-Uniqid
#!RemoteAsset:  sha256:b6919ba49b9fe98bfdf3e8accae7b9b7f78dc9e71ebbd0b7fef7a45d99324ccb
Source0:        https://www.cpan.org/authors/id/M/MW/MWX/Data-Uniqid-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
Data::Uniqid provides three simple routines for generating unique ids.
These ids are coded with a Base62 systen to make them short and handy (e.g.
to use it as part of a URL).

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
