# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-autovivification
Version:        0.18
Release:        %autorelease
Summary:        Lexically disable autovivification
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/autovivification
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/V/VP/VPIT/autovivification-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.3
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)

%description
When an undefined variable is dereferenced, it gets silently upgraded to an
array or hash reference (depending of the type of the dereferencing). This
behaviour is called autovivification and usually does what you mean (e.g.
when you store a value) but it may be unnatural or surprising because your
variables gets populated behind your back. This is especially true when
several levels of dereferencing are involved, in which case all levels are
vivified up to the last, or when it happens in intuitively read-only
constructs like exists.

%prep
%setup -q -n autovivification-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
