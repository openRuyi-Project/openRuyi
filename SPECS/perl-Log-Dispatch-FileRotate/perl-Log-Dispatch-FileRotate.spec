# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Log-Dispatch-FileRotate
Version:        1.38
Release:        %autorelease
Summary:        Log to Files that Archive/Rotate Themselves
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Log-Dispatch-FileRotate
#!RemoteAsset:  sha256:b55d6cede3f0a06426488fbfa554f4561320b014c1023893ced29508e5bce4ec
Source0:        https://www.cpan.org/authors/id/M/MS/MSCHOUT/Log-Dispatch-FileRotate-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Log::Dispatch) >= 2.60
BuildRequires:  perl(Log::Dispatch::File)
BuildRequires:  perl(Log::Dispatch::Output)
BuildRequires:  perl(Log::Dispatch::Screen)
BuildRequires:  perl(Params::ValidationCompiler)
BuildRequires:  perl(Path::Tiny) >= 0.018
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(utf8)
BuildRequires:  perl(Clone)
BuildRequires:  perl(version)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Eval::Closure)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Try::Tiny)

Requires:       perl(Log::Dispatch) >= 2.60

%description
This module extends the base class Log::Dispatch::Output to provides a
simple object for logging to files under the Log::Dispatch::* system, and
automatically rotating them according to different constraints. This is
basically a Log::Dispatch::File wrapper with additions.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
