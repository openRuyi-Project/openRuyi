# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           apimachinery
%define go_import_path  k8s.io/apimachinery
# These managedfields tests require Kubernetes repository fixtures that are not
# shipped in the standalone apimachinery module, and OBS fails opening
# api/openapi-spec/swagger.json. - HNO3Miracle
%define go_test_exclude %{shrink:
    k8s.io/apimachinery/pkg/util/managedfields
    k8s.io/apimachinery/pkg/util/managedfields/internal
}

Name:           go-k8s-apimachinery
Version:        0.36.1
Release:        %autorelease
Summary:        Scheme, typing, encoding, decoding, and conversion packages for Kubernetes and Kubernetes-like API objects
License:        Apache-2.0
URL:            https://github.com/kubernetes/apimachinery
#!RemoteAsset:  sha256:be56b2c258ae7afd48aa6666c27014348246546330dfbb9bd4d1ec376cee7477
Source0:        https://github.com/kubernetes/apimachinery/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/fxamacker/cbor/v2)
BuildRequires:  go(github.com/google/gnostic-models)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/mxk/go-flowrate)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(gopkg.in/evanphx/json-patch.v4)
BuildRequires:  go(gopkg.in/inf.v0)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(k8s.io/klog/v2/ktesting)
BuildRequires:  go(k8s.io/klog/v2/textlogger)
BuildRequires:  go(k8s.io/kube-openapi)
BuildRequires:  go(k8s.io/streaming)
BuildRequires:  go(k8s.io/utils)
BuildRequires:  go(sigs.k8s.io/json)
BuildRequires:  go(sigs.k8s.io/randfill)
BuildRequires:  go(sigs.k8s.io/structured-merge-diff/v6)
BuildRequires:  go(sigs.k8s.io/yaml)

Provides:       go(k8s.io/apimachinery) = %{version}
Provides:       go(k8s.io/apimachinery/pkg) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/apitesting) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/apitesting/fuzzer) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/apitesting/naming) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/apitesting/roundtrip) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/equality) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/errors) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/meta) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/meta/table) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/meta/testrestmapper) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/operation) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/resource) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/safe) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/validate) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/validate/constraints) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/validate/content) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/validation) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/validation/path) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/asn1) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/meta/fuzzer) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/meta/internalversion) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/meta/internalversion/scheme) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/meta/internalversion/validation) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/meta/v1) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured/unstructuredscheme) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/meta/v1/validation) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/meta/v1beta1) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/meta/v1beta1/validation) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/testapigroup) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/testapigroup/fuzzer) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/testapigroup/install) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/testapigroup/v1) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/conversion) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/conversion/queryparams) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/fields) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/labels) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/schema) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/serializer) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/serializer/cbor) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/serializer/cbor/direct) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/serializer/cbor/internal/modes) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/serializer/json) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/serializer/protobuf) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/serializer/recognizer) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/serializer/streaming) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/serializer/versioning) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/serializer/yaml) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/testing) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/testing/v1) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/selection) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/sharding) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/test) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/types) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/cache) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/diff) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/dump) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/duration) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/errors) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/framer) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/httpstream) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/httpstream/spdy) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/httpstream/wsstream) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/intstr) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/json) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/jsonmergepatch) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/managedfields) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/managedfields/internal) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/managedfields/internal/testing) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/managedfields/managedfieldstest) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/mergepatch) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/naming) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/net) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/net/testing) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/portforward) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/proxy) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/rand) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/remotecommand) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/resourceversion) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/runtime) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/sets) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/sort) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/strategicpatch) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/strategicpatch/testing) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/uuid) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/validation) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/validation/field) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/version) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/wait) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/waitgroup) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/yaml) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/version) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/watch) = %{version}
Provides:       go(k8s.io/apimachinery/third_party/forked/golang/json) = %{version}
Provides:       go(k8s.io/apimachinery/third_party/forked/golang/netutil) = %{version}
Provides:       go(k8s.io/apimachinery/third_party/forked/golang/reflect) = %{version}

Requires:       go(github.com/fxamacker/cbor/v2)
Requires:       go(github.com/google/gnostic-models)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/mxk/go-flowrate)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/spf13/pflag)
Requires:       go(golang.org/x/net)
Requires:       go(gopkg.in/evanphx/json-patch.v4)
Requires:       go(gopkg.in/inf.v0)
Requires:       go(k8s.io/klog/v2)
Requires:       go(k8s.io/klog/v2/textlogger)
Requires:       go(k8s.io/kube-openapi)
Requires:       go(k8s.io/streaming)
Requires:       go(k8s.io/utils)
Requires:       go(sigs.k8s.io/json)
Requires:       go(sigs.k8s.io/randfill)
Requires:       go(sigs.k8s.io/structured-merge-diff/v6)
Requires:       go(sigs.k8s.io/yaml)


%description
apimachinery contains the common runtime machinery shared by Kubernetes API
packages and clients. It provides schema handling, serializers, validation,
resource types, version helpers, watches, and utility packages used throughout
the Kubernetes Go dependency graph.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
