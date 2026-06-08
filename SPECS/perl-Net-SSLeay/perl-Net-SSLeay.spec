# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Net-SSLeay
Version:        1.96
Release:        %autorelease
Summary:        Perl bindings for OpenSSL and LibreSSL
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Net-SSLeay
#!RemoteAsset:  sha256:ab213691685fb2a576c669cbc8d9266f8165a31563ad15b7c4030b94adfc0753
Source0:        https://www.cpan.org/authors/id/C/CH/CHRISN/Net-SSLeay-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl-devel
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(SelectSaver)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More) >= 0.60_01
BuildRequires:  pkgconfig(openssl)

%description
This module provides Perl bindings for libssl (an SSL/TLS API) and
libcrypto (a cryptography API).

%files -f %{name}.files
%doc Changes CONTRIBUTING.md Credits QuickRef README README.OSX README.VMS README.Win32

%changelog
%autochangelog
