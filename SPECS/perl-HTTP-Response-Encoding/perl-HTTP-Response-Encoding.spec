# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-HTTP-Response-Encoding
Version:        0.06
Release:        %autorelease
Summary:        HTTP::Response::Encoding Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/HTTP-Response-Encoding
#!RemoteAsset:  sha256:10167b8e238a682004ab0d7accbe9d76eae2db57af07c5ae2dfa808074a4a8aa
Source0:        https://www.cpan.org/authors/id/D/DA/DANKOGAI/HTTP-Response-Encoding-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(Encode) >= 2
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(IO::HTML)

Requires:       perl(Encode) >= 2

%description
SYNOPSIS      use LWP::UserAgent;      use HTTP::Response::Encoding;

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
