# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: laokz <zhangkai@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fakeroot
Version:        1.37.2
Release:        %autorelease
Summary:        Gives a fake root environment
License:        GPL-3.0-or-later
URL:            https://tracker.debian.org/pkg/fakeroot
VCS:            git:https://salsa.debian.org/clint/fakeroot
#!RemoteAsset
Source:         https://deb.debian.org/debian/pool/main/f/fakeroot/fakeroot_%{version}.orig.tar.gz
BuildSystem:    autotools

Patch0:         debian_fix-shell-in-fakeroot.patch

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  util-linux
BuildRequires:  gcc
BuildRequires:  acl-devel
BuildRequires:  libcap-devel
BuildRequires:  sharutils
Requires(post): alternatives
Requires(post): coreutils
Requires(preun): alternatives

%description
fakeroot runs a command in an environment wherein it appears to have
root privileges for file manipulation. fakeroot works by replacing the
file manipulation library functions (chmod(2), stat(2) etc.) by ones
that simulate the effect the real library functions would have had,
had the user really been root.

%conf
./bootstrap

%build
for type in sysv tcp; do
  mkdir obj-$type
  cd obj-$type
  cat >> configure << 'EOF'
#!/bin/sh
exec ../configure "$@"
EOF
  chmod +x configure
  %configure \
    --disable-dependency-tracking \
    --disable-static \
    --libdir=%{_libdir}/libfakeroot \
    --with-ipc=$type \
    --program-suffix=-$type
  make
  cd ..
done

%install
for type in sysv tcp; do
  make -C obj-$type install libdir=%{_libdir}/libfakeroot DESTDIR=%{buildroot}
  mv %{buildroot}%{_libdir}/libfakeroot/libfakeroot-0.so \
     %{buildroot}%{_libdir}/libfakeroot/libfakeroot-$type.so
  rm -f %{buildroot}%{_libdir}/libfakeroot/libfakeroot.so
  %find_lang faked-$type --without-mo --with-man
  %find_lang fakeroot-$type --without-mo --with-man
done

rm %{buildroot}%{_mandir}{,/*}/man1/fake{d,root}-sysv.1
rename -- -tcp '' %{buildroot}%{_mandir}{,/*}/man1/fake{d,root}-tcp.1
sed -e 's/-tcp//g' fake{d,root}-tcp.lang > fakeroot.lang

%check
for type in sysv tcp; do
  make -C obj-$type check VERBOSE=1
done

%post
link=$(readlink -e "/usr/bin/fakeroot")
if [ "$link" = "/usr/bin/fakeroot" ]; then
  rm -f /usr/bin/fakeroot
fi
link=$(readlink -e "%{_bindir}/faked")
if [ "$link" = "%{_bindir}/faked" ]; then
  rm -f "%{_bindir}/faked"
fi
link=$(readlink -e "%{_libdir}/libfakeroot/libfakeroot-0.so")
if [ "$link" = "%{_libdir}/libfakeroot/libfakeroot-0.so" ]; then
  rm -f "%{_libdir}/libfakeroot/libfakeroot-0.so"
fi

alternatives --install "%{_bindir}/fakeroot" fakeroot \
  "%{_bindir}/fakeroot-tcp" 50 \
  --follower %{_bindir}/faked faked %{_bindir}/faked-tcp \
  --follower %{_libdir}/libfakeroot/libfakeroot-0.so libfakeroot.so %{_libdir}/libfakeroot/libfakeroot-tcp.so

alternatives --install "%{_bindir}/fakeroot" fakeroot \
  "%{_bindir}/fakeroot-sysv" 40 \
  --follower %{_bindir}/faked faked %{_bindir}/faked-sysv \
  --follower %{_libdir}/libfakeroot/libfakeroot-0.so libfakeroot.so %{_libdir}/libfakeroot/libfakeroot-sysv.so || :

%preun
if [ $1 = 0 ]; then
  alternatives --remove fakeroot "%{_bindir}/fakeroot-tcp"
  alternatives --remove fakeroot "%{_bindir}/fakeroot-sysv" || :
fi

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING AUTHORS BUGS DEBUG doc/README.saving
%{_bindir}/faked-*
%ghost %{_bindir}/faked
%{_bindir}/fakeroot-*
%ghost %{_bindir}/fakeroot
%{_mandir}/man1/faked.1*
%{_mandir}/man1/fakeroot.1*

%dir %{_libdir}/libfakeroot
%{_libdir}/libfakeroot/libfakeroot-sysv.so
%{_libdir}/libfakeroot/libfakeroot-tcp.so
%ghost %{_libdir}/libfakeroot/libfakeroot-0.so

%changelog
%autochangelog
