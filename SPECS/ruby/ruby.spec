# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global ruby_api_version 4.0.0
%global ruby_soversion 4.0
%global rubygems_version 4.0.10
%global ruby_arch %{_arch}-linux
%global ruby_librubydir %{_libdir}/ruby/%{ruby_api_version}
%global ruby_gemdir %{_libdir}/ruby/gems/%{ruby_api_version}
%global ruby_gemextdir %{ruby_gemdir}/extensions/%{ruby_arch}/%{ruby_api_version}

Name:           ruby
Version:        4.0.3
Release:        %autorelease
Summary:        Ruby programming language interpreter
License:        (Ruby OR BSD-2-Clause) AND MIT
URL:            https://www.ruby-lang.org/
VCS:            git:https://github.com/ruby/ruby.git
#!RemoteAsset:  sha256:77964acc370d5c8375b9502e5ba6c13c03ef91ab9eb9f521c84fb42b9c9a6b0f
Source0:        https://cache.ruby-lang.org/pub/ruby/4.0/ruby-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --libdir=%{_libdir}
BuildOption(conf):  --libexecdir=%{_libdir}/ruby
BuildOption(conf):  --enable-shared
BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-rpath
BuildOption(conf):  --disable-yjit
BuildOption(conf):  --with-dbm-type=gdbm_compat

BuildRequires:  bison
BuildRequires:  gdbm-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(zlib)

Provides:       ruby(abi) = %{ruby_soversion}
Provides:       rubygems = %{rubygems_version}

%description
Ruby is an interpreted, object-oriented programming language focused on
developer productivity. This package provides the Ruby interpreter, the core
standard library, and the runtime shared library.

%package        devel
Summary:        Header files and development files for Ruby
License:        Ruby OR BSD-2-Clause
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package provides the header files, pkg-config metadata, and development
link needed to build C extensions and applications embedding Ruby.

%package        doc
Summary:        Documentation for Ruby
License:        (Ruby OR BSD-2-Clause) AND MIT
BuildArch:      noarch

%description    doc
This package contains the upstream Ruby documentation and any generated ri or
rdoc content installed during the build.

%prep
%autosetup -n %{name}-%{version}

%conf -p
autoreconf -fiv

%install -a
ln -sfn libruby.so.%{version} %{buildroot}%{_libdir}/libruby.so.%{ruby_soversion}
ln -sfn libruby.so.%{ruby_soversion} %{buildroot}%{_libdir}/libruby.so

mkdir -p %{buildroot}%{_libdir}/pkgconfig
(
    cd %{buildroot}%{_libdir}/pkgconfig
    ln -sfn ruby-4.0.pc ruby.pc
)

find %{buildroot} \
    \( -name '*.o' -o -name Makefile -o -name config.log -o -name config.status -o -name Makefile.html -o -name gem_make.out -o -name mkmf.log -o -name '*.bak' -o -name .deps -o -name .libs -o -name CVS \) \
    -print0 | xargs -r0 rm -rv || :
# remove more strict in the docu
find %{buildroot} -type d -name '.gem.*' -print0 | xargs -r0 rm -rv || :
rm -rf %{buildroot}%{ruby_gemdir}/cache
find %{buildroot} -type f -name '*.pem' -delete

%check
%ifarch riscv64
# Ruby test-all currently times out or aborts in upstream tests on riscv64.
%make_build test
%else
# only run offline test suite
%make_build test test-all
%endif

%files
%license BSDL COPYING GPL LEGAL
%dir %{ruby_gemdir}
%dir %{ruby_gemdir}/extensions
%dir %{ruby_gemdir}/extensions/%{ruby_arch}
%dir %{ruby_gemdir}/gems
%dir %{ruby_gemdir}/plugins
%dir %{ruby_gemdir}/specifications
%dir %{ruby_gemdir}/specifications/default
%{_bindir}/ruby*
%{_bindir}/erb*
%{_bindir}/irb*
%{_bindir}/rdoc*
%{_bindir}/ri*
%{_bindir}/gem*
%{_bindir}/minitest
%{_bindir}/racc
%{_bindir}/rake*
%{_bindir}/rbs
%{_bindir}/rdbg
%{_bindir}/syntax_suggest
%{_bindir}/test-unit
%{_bindir}/typeprof
%{_bindir}/bundle*
%{_mandir}/man1/erb*.1%{?ext_man}
%{_mandir}/man1/ruby*.1%{?ext_man}
%{_libdir}/libruby.so.*
%{ruby_librubydir}
%{ruby_gemextdir}
%{ruby_gemdir}/gems/*
%{ruby_gemdir}/plugins/*
%{ruby_gemdir}/specifications/*.gemspec
%{ruby_gemdir}/specifications/default/*.gemspec

%files devel
%{_includedir}/ruby-%{ruby_api_version}
%{_libdir}/libruby.so
%{_libdir}/pkgconfig/ruby-4.0.pc
%{_libdir}/pkgconfig/ruby.pc

%files doc
%doc NEWS* README* doc
%dir %{_datadir}/ri
%{_datadir}/ri/*

%changelog
%autochangelog
