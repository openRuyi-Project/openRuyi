# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Hook-LexWrap
Version:        0.26
Release:        %autorelease
Summary:        Lexically scoped subroutine wrappers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Hook-LexWrap
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/Hook-LexWrap-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
Hook::LexWrap allows you to install a pre- or post-wrapper (or both) around
an existing subroutine. Unlike other modules that provide this capacity
(e.g. Hook::PreAndPost and Hook::WrapSub), Hook::LexWrap implements
wrappers in such a way that the standard caller function works correctly
within the wrapped subroutine.

%prep
%setup -q -n Hook-LexWrap-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING README

%changelog
%autochangelog
