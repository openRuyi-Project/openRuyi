# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           client-go
%define go_import_path  k8s.io/client-go

Name:           go-k8s-client-go
Version:        1.36.0~alpha2
Release:        %autorelease
Summary:        Go client for Kubernetes.
License:        Apache-2.0
URL:            https://github.com/kubernetes/client-go
#!RemoteAsset:  sha256:b5727b2717ef2f83af80607c47995d4b31874cbb0b42a886df91df58ad088328
Source0:        https://github.com/kubernetes/client-go/archive/refs/tags/kubernetes-1.36.0-alpha.2.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n client-go-kubernetes-1.36.0-alpha.2
# k8s.io/client-go/testing/internal and k8s.io/client-go/tools/cache use
# testing/synctest; OBS builds run with asynctimerchan!=0, which makes
# synctest.Run panic with "synctest.Run not supported with asynctimerchan!=0".
# k8s.io/client-go/tools/remotecommand HTTPS proxy tests fail in OBS with
# "proxy: unknown scheme: https"; keep the rest of client-go tests enabled.
%define go_test_exclude %{shrink:
    %{go_import_path}/testing/internal
    %{go_import_path}/tools/cache
    %{go_import_path}/tools/remotecommand
}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/emicklei/go-restful/v3)
BuildRequires:  go(github.com/fxamacker/cbor/v2)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/logr/funcr)
BuildRequires:  go(github.com/go-openapi/jsonpointer)
BuildRequires:  go(github.com/go-openapi/jsonreference)
BuildRequires:  go(github.com/go-openapi/swag)
BuildRequires:  go(github.com/google/btree)
BuildRequires:  go(github.com/google/gnostic-models)
BuildRequires:  go(github.com/google/gnostic-models/openapiv2)
BuildRequires:  go(github.com/google/gnostic-models/openapiv3)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-cmp/cmp)
BuildRequires:  go(github.com/google/go-cmp/cmp/cmpopts)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/josharian/intern)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/mailru/easyjson)
BuildRequires:  go(github.com/moby/spdystream)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/munnerz/goautoneg)
BuildRequires:  go(github.com/mxk/go-flowrate)
BuildRequires:  go(github.com/peterbourgon/diskv)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/stretchr/objx)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/stretchr/testify/assert)
BuildRequires:  go(github.com/stretchr/testify/mock)
BuildRequires:  go(github.com/stretchr/testify/require)
BuildRequires:  go(github.com/x448/float16)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/net/http2)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(golang.org/x/time/rate)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(google.golang.org/protobuf/proto)
BuildRequires:  go(gopkg.in/evanphx/json-patch.v4)
BuildRequires:  go(gopkg.in/inf.v0)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(k8s.io/api)
BuildRequires:  go(k8s.io/api/admissionregistration/v1)
BuildRequires:  go(k8s.io/api/admissionregistration/v1alpha1)
BuildRequires:  go(k8s.io/api/admissionregistration/v1beta1)
BuildRequires:  go(k8s.io/api/apidiscovery/v2)
BuildRequires:  go(k8s.io/api/apidiscovery/v2beta1)
BuildRequires:  go(k8s.io/api/apiserverinternal/v1alpha1)
BuildRequires:  go(k8s.io/api/apps/v1)
BuildRequires:  go(k8s.io/api/apps/v1beta1)
BuildRequires:  go(k8s.io/api/apps/v1beta2)
BuildRequires:  go(k8s.io/api/authentication/v1)
BuildRequires:  go(k8s.io/api/authentication/v1alpha1)
BuildRequires:  go(k8s.io/api/authentication/v1beta1)
BuildRequires:  go(k8s.io/api/authorization/v1)
BuildRequires:  go(k8s.io/api/authorization/v1beta1)
BuildRequires:  go(k8s.io/api/autoscaling/v1)
BuildRequires:  go(k8s.io/api/autoscaling/v2)
BuildRequires:  go(k8s.io/api/batch/v1)
BuildRequires:  go(k8s.io/api/batch/v1beta1)
BuildRequires:  go(k8s.io/api/certificates/v1)
BuildRequires:  go(k8s.io/api/certificates/v1alpha1)
BuildRequires:  go(k8s.io/api/certificates/v1beta1)
BuildRequires:  go(k8s.io/api/coordination/v1)
BuildRequires:  go(k8s.io/api/coordination/v1alpha2)
BuildRequires:  go(k8s.io/api/coordination/v1beta1)
BuildRequires:  go(k8s.io/api/core/v1)
BuildRequires:  go(k8s.io/api/discovery/v1)
BuildRequires:  go(k8s.io/api/discovery/v1beta1)
BuildRequires:  go(k8s.io/api/events/v1)
BuildRequires:  go(k8s.io/api/events/v1beta1)
BuildRequires:  go(k8s.io/api/extensions/v1beta1)
BuildRequires:  go(k8s.io/api/flowcontrol/v1)
BuildRequires:  go(k8s.io/api/flowcontrol/v1beta1)
BuildRequires:  go(k8s.io/api/flowcontrol/v1beta2)
BuildRequires:  go(k8s.io/api/flowcontrol/v1beta3)
BuildRequires:  go(k8s.io/api/imagepolicy/v1alpha1)
BuildRequires:  go(k8s.io/api/networking/v1)
BuildRequires:  go(k8s.io/api/networking/v1beta1)
BuildRequires:  go(k8s.io/api/node/v1)
BuildRequires:  go(k8s.io/api/node/v1alpha1)
BuildRequires:  go(k8s.io/api/node/v1beta1)
BuildRequires:  go(k8s.io/api/policy/v1)
BuildRequires:  go(k8s.io/api/policy/v1beta1)
BuildRequires:  go(k8s.io/api/rbac/v1)
BuildRequires:  go(k8s.io/api/rbac/v1alpha1)
BuildRequires:  go(k8s.io/api/rbac/v1beta1)
BuildRequires:  go(k8s.io/api/resource/v1)
BuildRequires:  go(k8s.io/api/resource/v1alpha3)
BuildRequires:  go(k8s.io/api/resource/v1beta1)
BuildRequires:  go(k8s.io/api/resource/v1beta2)
BuildRequires:  go(k8s.io/api/scheduling/v1)
BuildRequires:  go(k8s.io/api/scheduling/v1alpha1)
BuildRequires:  go(k8s.io/api/scheduling/v1beta1)
BuildRequires:  go(k8s.io/api/storage/v1)
BuildRequires:  go(k8s.io/api/storage/v1alpha1)
BuildRequires:  go(k8s.io/api/storage/v1beta1)
BuildRequires:  go(k8s.io/api/storagemigration/v1beta1)
BuildRequires:  go(k8s.io/apimachinery)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/apitesting/roundtrip)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/equality)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/errors)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/meta)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/meta/testrestmapper)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/resource)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/validation)
BuildRequires:  go(k8s.io/apimachinery/pkg/apis/meta/internalversion)
BuildRequires:  go(k8s.io/apimachinery/pkg/apis/meta/internalversion/scheme)
BuildRequires:  go(k8s.io/apimachinery/pkg/apis/meta/internalversion/validation)
BuildRequires:  go(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  go(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured)
BuildRequires:  go(k8s.io/apimachinery/pkg/apis/meta/v1beta1)
BuildRequires:  go(k8s.io/apimachinery/pkg/conversion)
BuildRequires:  go(k8s.io/apimachinery/pkg/fields)
BuildRequires:  go(k8s.io/apimachinery/pkg/labels)
BuildRequires:  go(k8s.io/apimachinery/pkg/runtime)
BuildRequires:  go(k8s.io/apimachinery/pkg/runtime/schema)
BuildRequires:  go(k8s.io/apimachinery/pkg/runtime/serializer)
BuildRequires:  go(k8s.io/apimachinery/pkg/runtime/serializer/cbor)
BuildRequires:  go(k8s.io/apimachinery/pkg/runtime/serializer/cbor/direct)
BuildRequires:  go(k8s.io/apimachinery/pkg/runtime/serializer/json)
BuildRequires:  go(k8s.io/apimachinery/pkg/runtime/serializer/streaming)
BuildRequires:  go(k8s.io/apimachinery/pkg/runtime/serializer/versioning)
BuildRequires:  go(k8s.io/apimachinery/pkg/types)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/cache)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/diff)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/errors)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/httpstream)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/httpstream/spdy)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/httpstream/wsstream)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/intstr)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/json)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/managedfields)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/naming)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/net)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/net/testing)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/portforward)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/rand)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/remotecommand)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/runtime)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/sets)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/strategicpatch)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/validation)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/version)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/wait)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/yaml)
BuildRequires:  go(k8s.io/apimachinery/pkg/version)
BuildRequires:  go(k8s.io/apimachinery/pkg/watch)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(k8s.io/klog/v2/ktesting)
BuildRequires:  go(k8s.io/klog/v2/ktesting/init)
BuildRequires:  go(k8s.io/klog/v2/textlogger)
BuildRequires:  go(k8s.io/kube-openapi)
BuildRequires:  go(k8s.io/kube-openapi/pkg/handler3)
BuildRequires:  go(k8s.io/kube-openapi/pkg/spec3)
BuildRequires:  go(k8s.io/kube-openapi/pkg/util/proto)
BuildRequires:  go(k8s.io/kube-openapi/pkg/validation/spec)
BuildRequires:  go(k8s.io/utils)
BuildRequires:  go(k8s.io/utils/buffer)
BuildRequires:  go(k8s.io/utils/clock)
BuildRequires:  go(k8s.io/utils/clock/testing)
BuildRequires:  go(k8s.io/utils/dump)
BuildRequires:  go(k8s.io/utils/lru)
BuildRequires:  go(k8s.io/utils/net)
BuildRequires:  go(k8s.io/utils/ptr)
BuildRequires:  go(k8s.io/utils/trace)
BuildRequires:  go(sigs.k8s.io/json)
BuildRequires:  go(sigs.k8s.io/randfill)
BuildRequires:  go(sigs.k8s.io/structured-merge-diff/v6)
BuildRequires:  go(sigs.k8s.io/structured-merge-diff/v6/fieldpath)
BuildRequires:  go(sigs.k8s.io/structured-merge-diff/v6/typed)
BuildRequires:  go(sigs.k8s.io/yaml)

Provides:       go(k8s.io/client-go) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/admissionregistration/v1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/admissionregistration/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/admissionregistration/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/apiserverinternal/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/apps/v1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/apps/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/apps/v1beta2) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/autoscaling/v1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/autoscaling/v2) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/batch/v1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/batch/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/certificates/v1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/certificates/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/certificates/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/coordination/v1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/coordination/v1alpha2) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/coordination/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/core/v1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/discovery/v1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/discovery/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/events/v1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/events/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/extensions/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/flowcontrol/v1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/flowcontrol/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/flowcontrol/v1beta2) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/flowcontrol/v1beta3) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/imagepolicy/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/internal) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/meta/v1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/networking/v1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/networking/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/node/v1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/node/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/node/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/policy/v1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/policy/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/rbac/v1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/rbac/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/rbac/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/resource/v1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/resource/v1alpha3) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/resource/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/resource/v1beta2) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/scheduling/v1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/scheduling/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/scheduling/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/storage/v1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/storage/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/storage/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/applyconfigurations/storagemigration/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/discovery) = %{version}
Provides:       go(k8s.io/client-go/discovery/cached) = %{version}
Provides:       go(k8s.io/client-go/discovery/cached/disk) = %{version}
Provides:       go(k8s.io/client-go/discovery/cached/memory) = %{version}
Provides:       go(k8s.io/client-go/discovery/fake) = %{version}
Provides:       go(k8s.io/client-go/dynamic) = %{version}
Provides:       go(k8s.io/client-go/dynamic/dynamicinformer) = %{version}
Provides:       go(k8s.io/client-go/dynamic/dynamiclister) = %{version}
Provides:       go(k8s.io/client-go/dynamic/fake) = %{version}
Provides:       go(k8s.io/client-go/features) = %{version}
Provides:       go(k8s.io/client-go/features/testing) = %{version}
Provides:       go(k8s.io/client-go/gentype) = %{version}
Provides:       go(k8s.io/client-go/informers) = %{version}
Provides:       go(k8s.io/client-go/informers/admissionregistration) = %{version}
Provides:       go(k8s.io/client-go/informers/admissionregistration/v1) = %{version}
Provides:       go(k8s.io/client-go/informers/admissionregistration/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/informers/admissionregistration/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/informers/apiserverinternal) = %{version}
Provides:       go(k8s.io/client-go/informers/apiserverinternal/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/informers/apps) = %{version}
Provides:       go(k8s.io/client-go/informers/apps/v1) = %{version}
Provides:       go(k8s.io/client-go/informers/apps/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/informers/apps/v1beta2) = %{version}
Provides:       go(k8s.io/client-go/informers/autoscaling) = %{version}
Provides:       go(k8s.io/client-go/informers/autoscaling/v1) = %{version}
Provides:       go(k8s.io/client-go/informers/autoscaling/v2) = %{version}
Provides:       go(k8s.io/client-go/informers/batch) = %{version}
Provides:       go(k8s.io/client-go/informers/batch/v1) = %{version}
Provides:       go(k8s.io/client-go/informers/batch/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/informers/certificates) = %{version}
Provides:       go(k8s.io/client-go/informers/certificates/v1) = %{version}
Provides:       go(k8s.io/client-go/informers/certificates/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/informers/certificates/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/informers/coordination) = %{version}
Provides:       go(k8s.io/client-go/informers/coordination/v1) = %{version}
Provides:       go(k8s.io/client-go/informers/coordination/v1alpha2) = %{version}
Provides:       go(k8s.io/client-go/informers/coordination/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/informers/core) = %{version}
Provides:       go(k8s.io/client-go/informers/core/v1) = %{version}
Provides:       go(k8s.io/client-go/informers/discovery) = %{version}
Provides:       go(k8s.io/client-go/informers/discovery/v1) = %{version}
Provides:       go(k8s.io/client-go/informers/discovery/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/informers/events) = %{version}
Provides:       go(k8s.io/client-go/informers/events/v1) = %{version}
Provides:       go(k8s.io/client-go/informers/events/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/informers/extensions) = %{version}
Provides:       go(k8s.io/client-go/informers/extensions/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/informers/flowcontrol) = %{version}
Provides:       go(k8s.io/client-go/informers/flowcontrol/v1) = %{version}
Provides:       go(k8s.io/client-go/informers/flowcontrol/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/informers/flowcontrol/v1beta2) = %{version}
Provides:       go(k8s.io/client-go/informers/flowcontrol/v1beta3) = %{version}
Provides:       go(k8s.io/client-go/informers/internalinterfaces) = %{version}
Provides:       go(k8s.io/client-go/informers/networking) = %{version}
Provides:       go(k8s.io/client-go/informers/networking/v1) = %{version}
Provides:       go(k8s.io/client-go/informers/networking/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/informers/node) = %{version}
Provides:       go(k8s.io/client-go/informers/node/v1) = %{version}
Provides:       go(k8s.io/client-go/informers/node/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/informers/node/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/informers/policy) = %{version}
Provides:       go(k8s.io/client-go/informers/policy/v1) = %{version}
Provides:       go(k8s.io/client-go/informers/policy/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/informers/rbac) = %{version}
Provides:       go(k8s.io/client-go/informers/rbac/v1) = %{version}
Provides:       go(k8s.io/client-go/informers/rbac/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/informers/rbac/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/informers/resource) = %{version}
Provides:       go(k8s.io/client-go/informers/resource/v1) = %{version}
Provides:       go(k8s.io/client-go/informers/resource/v1alpha3) = %{version}
Provides:       go(k8s.io/client-go/informers/resource/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/informers/resource/v1beta2) = %{version}
Provides:       go(k8s.io/client-go/informers/scheduling) = %{version}
Provides:       go(k8s.io/client-go/informers/scheduling/v1) = %{version}
Provides:       go(k8s.io/client-go/informers/scheduling/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/informers/scheduling/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/informers/storage) = %{version}
Provides:       go(k8s.io/client-go/informers/storage/v1) = %{version}
Provides:       go(k8s.io/client-go/informers/storage/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/informers/storage/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/informers/storagemigration) = %{version}
Provides:       go(k8s.io/client-go/informers/storagemigration/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/scheme) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/admissionregistration/v1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/admissionregistration/v1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/admissionregistration/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/admissionregistration/v1alpha1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/admissionregistration/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/admissionregistration/v1beta1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/apiserverinternal/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/apiserverinternal/v1alpha1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/apps/v1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/apps/v1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/apps/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/apps/v1beta1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/apps/v1beta2) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/apps/v1beta2/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/authentication/v1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/authentication/v1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/authentication/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/authentication/v1alpha1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/authentication/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/authentication/v1beta1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/authorization/v1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/authorization/v1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/authorization/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/authorization/v1beta1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/autoscaling/v1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/autoscaling/v1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/autoscaling/v2) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/autoscaling/v2/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/batch/v1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/batch/v1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/batch/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/batch/v1beta1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/certificates/v1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/certificates/v1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/certificates/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/certificates/v1alpha1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/certificates/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/certificates/v1beta1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/coordination/v1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/coordination/v1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/coordination/v1alpha2) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/coordination/v1alpha2/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/coordination/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/coordination/v1beta1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/core/v1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/core/v1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/discovery/v1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/discovery/v1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/discovery/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/discovery/v1beta1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/events/v1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/events/v1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/events/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/events/v1beta1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/extensions/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/extensions/v1beta1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/flowcontrol/v1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/flowcontrol/v1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/flowcontrol/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/flowcontrol/v1beta1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/flowcontrol/v1beta2) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/flowcontrol/v1beta2/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/flowcontrol/v1beta3) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/flowcontrol/v1beta3/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/networking/v1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/networking/v1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/networking/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/networking/v1beta1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/node/v1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/node/v1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/node/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/node/v1alpha1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/node/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/node/v1beta1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/policy/v1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/policy/v1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/policy/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/policy/v1beta1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/rbac/v1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/rbac/v1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/rbac/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/rbac/v1alpha1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/rbac/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/rbac/v1beta1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/resource/v1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/resource/v1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/resource/v1alpha3) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/resource/v1alpha3/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/resource/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/resource/v1beta1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/resource/v1beta2) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/resource/v1beta2/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/scheduling/v1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/scheduling/v1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/scheduling/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/scheduling/v1alpha1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/scheduling/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/scheduling/v1beta1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/storage/v1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/storage/v1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/storage/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/storage/v1alpha1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/storage/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/storage/v1beta1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/storagemigration/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/kubernetes/typed/storagemigration/v1beta1/fake) = %{version}
Provides:       go(k8s.io/client-go/kubernetes_test) = %{version}
Provides:       go(k8s.io/client-go/listers) = %{version}
Provides:       go(k8s.io/client-go/listers/admissionregistration/v1) = %{version}
Provides:       go(k8s.io/client-go/listers/admissionregistration/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/listers/admissionregistration/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/listers/apiserverinternal/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/listers/apps/v1) = %{version}
Provides:       go(k8s.io/client-go/listers/apps/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/listers/apps/v1beta2) = %{version}
Provides:       go(k8s.io/client-go/listers/autoscaling/v1) = %{version}
Provides:       go(k8s.io/client-go/listers/autoscaling/v2) = %{version}
Provides:       go(k8s.io/client-go/listers/batch/v1) = %{version}
Provides:       go(k8s.io/client-go/listers/batch/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/listers/certificates/v1) = %{version}
Provides:       go(k8s.io/client-go/listers/certificates/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/listers/certificates/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/listers/coordination/v1) = %{version}
Provides:       go(k8s.io/client-go/listers/coordination/v1alpha2) = %{version}
Provides:       go(k8s.io/client-go/listers/coordination/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/listers/core/v1) = %{version}
Provides:       go(k8s.io/client-go/listers/discovery/v1) = %{version}
Provides:       go(k8s.io/client-go/listers/discovery/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/listers/events/v1) = %{version}
Provides:       go(k8s.io/client-go/listers/events/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/listers/extensions/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/listers/flowcontrol/v1) = %{version}
Provides:       go(k8s.io/client-go/listers/flowcontrol/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/listers/flowcontrol/v1beta2) = %{version}
Provides:       go(k8s.io/client-go/listers/flowcontrol/v1beta3) = %{version}
Provides:       go(k8s.io/client-go/listers/imagepolicy/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/listers/networking/v1) = %{version}
Provides:       go(k8s.io/client-go/listers/networking/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/listers/node/v1) = %{version}
Provides:       go(k8s.io/client-go/listers/node/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/listers/node/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/listers/policy/v1) = %{version}
Provides:       go(k8s.io/client-go/listers/policy/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/listers/rbac/v1) = %{version}
Provides:       go(k8s.io/client-go/listers/rbac/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/listers/rbac/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/listers/resource/v1) = %{version}
Provides:       go(k8s.io/client-go/listers/resource/v1alpha3) = %{version}
Provides:       go(k8s.io/client-go/listers/resource/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/listers/resource/v1beta2) = %{version}
Provides:       go(k8s.io/client-go/listers/scheduling/v1) = %{version}
Provides:       go(k8s.io/client-go/listers/scheduling/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/listers/scheduling/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/listers/storage/v1) = %{version}
Provides:       go(k8s.io/client-go/listers/storage/v1alpha1) = %{version}
Provides:       go(k8s.io/client-go/listers/storage/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/listers/storagemigration/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/metadata) = %{version}
Provides:       go(k8s.io/client-go/metadata/fake) = %{version}
Provides:       go(k8s.io/client-go/metadata/metadatainformer) = %{version}
Provides:       go(k8s.io/client-go/metadata/metadatalister) = %{version}
Provides:       go(k8s.io/client-go/openapi) = %{version}
Provides:       go(k8s.io/client-go/openapi/cached) = %{version}
Provides:       go(k8s.io/client-go/openapi/openapitest) = %{version}
Provides:       go(k8s.io/client-go/openapi3) = %{version}
Provides:       go(k8s.io/client-go/pkg/apis/clientauthentication) = %{version}
Provides:       go(k8s.io/client-go/pkg/apis/clientauthentication/install) = %{version}
Provides:       go(k8s.io/client-go/pkg/apis/clientauthentication/v1) = %{version}
Provides:       go(k8s.io/client-go/pkg/apis/clientauthentication/v1beta1) = %{version}
Provides:       go(k8s.io/client-go/pkg/version) = %{version}
Provides:       go(k8s.io/client-go/plugin/pkg/client/auth) = %{version}
Provides:       go(k8s.io/client-go/plugin/pkg/client/auth/azure) = %{version}
Provides:       go(k8s.io/client-go/plugin/pkg/client/auth/exec) = %{version}
Provides:       go(k8s.io/client-go/plugin/pkg/client/auth/gcp) = %{version}
Provides:       go(k8s.io/client-go/plugin/pkg/client/auth/oidc) = %{version}
Provides:       go(k8s.io/client-go/rest) = %{version}
Provides:       go(k8s.io/client-go/rest/fake) = %{version}
Provides:       go(k8s.io/client-go/rest/watch) = %{version}
Provides:       go(k8s.io/client-go/restmapper) = %{version}
Provides:       go(k8s.io/client-go/scale) = %{version}
Provides:       go(k8s.io/client-go/scale/fake) = %{version}
Provides:       go(k8s.io/client-go/scale/scheme) = %{version}
Provides:       go(k8s.io/client-go/scale/scheme/appsint) = %{version}
Provides:       go(k8s.io/client-go/scale/scheme/appsv1beta1) = %{version}
Provides:       go(k8s.io/client-go/scale/scheme/appsv1beta2) = %{version}
Provides:       go(k8s.io/client-go/scale/scheme/autoscalingv1) = %{version}
Provides:       go(k8s.io/client-go/scale/scheme/extensionsint) = %{version}
Provides:       go(k8s.io/client-go/scale/scheme/extensionsv1beta1) = %{version}
Provides:       go(k8s.io/client-go/testing) = %{version}
Provides:       go(k8s.io/client-go/testing/internal) = %{version}
Provides:       go(k8s.io/client-go/third_party/forked/golang/template) = %{version}
Provides:       go(k8s.io/client-go/third_party/forked/httpcache) = %{version}
Provides:       go(k8s.io/client-go/tools/auth) = %{version}
Provides:       go(k8s.io/client-go/tools/auth/exec) = %{version}
Provides:       go(k8s.io/client-go/tools/cache) = %{version}
Provides:       go(k8s.io/client-go/tools/cache/synctrack) = %{version}
Provides:       go(k8s.io/client-go/tools/cache/testing) = %{version}
Provides:       go(k8s.io/client-go/tools/clientcmd) = %{version}
Provides:       go(k8s.io/client-go/tools/clientcmd/api) = %{version}
Provides:       go(k8s.io/client-go/tools/clientcmd/api/latest) = %{version}
Provides:       go(k8s.io/client-go/tools/clientcmd/api/v1) = %{version}
Provides:       go(k8s.io/client-go/tools/events) = %{version}
Provides:       go(k8s.io/client-go/tools/internal/events) = %{version}
Provides:       go(k8s.io/client-go/tools/leaderelection) = %{version}
Provides:       go(k8s.io/client-go/tools/leaderelection/resourcelock) = %{version}
Provides:       go(k8s.io/client-go/tools/metrics) = %{version}
Provides:       go(k8s.io/client-go/tools/pager) = %{version}
Provides:       go(k8s.io/client-go/tools/portforward) = %{version}
Provides:       go(k8s.io/client-go/tools/record) = %{version}
Provides:       go(k8s.io/client-go/tools/record/util) = %{version}
Provides:       go(k8s.io/client-go/tools/reference) = %{version}
Provides:       go(k8s.io/client-go/tools/remotecommand) = %{version}
Provides:       go(k8s.io/client-go/tools/watch) = %{version}
Provides:       go(k8s.io/client-go/transport) = %{version}
Provides:       go(k8s.io/client-go/transport/spdy) = %{version}
Provides:       go(k8s.io/client-go/transport/websocket) = %{version}
Provides:       go(k8s.io/client-go/util/apply) = %{version}
Provides:       go(k8s.io/client-go/util/cert) = %{version}
Provides:       go(k8s.io/client-go/util/certificate) = %{version}
Provides:       go(k8s.io/client-go/util/certificate/csr) = %{version}
Provides:       go(k8s.io/client-go/util/connrotation) = %{version}
Provides:       go(k8s.io/client-go/util/consistencydetector) = %{version}
Provides:       go(k8s.io/client-go/util/csaupgrade) = %{version}
Provides:       go(k8s.io/client-go/util/exec) = %{version}
Provides:       go(k8s.io/client-go/util/flowcontrol) = %{version}
Provides:       go(k8s.io/client-go/util/homedir) = %{version}
Provides:       go(k8s.io/client-go/util/jsonpath) = %{version}
Provides:       go(k8s.io/client-go/util/keyutil) = %{version}
Provides:       go(k8s.io/client-go/util/retry) = %{version}
Provides:       go(k8s.io/client-go/util/testing) = %{version}
Provides:       go(k8s.io/client-go/util/watchlist) = %{version}
Provides:       go(k8s.io/client-go/util/workqueue) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/emicklei/go-restful/v3)
Requires:       go(github.com/fxamacker/cbor/v2)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-openapi/jsonpointer)
Requires:       go(github.com/go-openapi/jsonreference)
Requires:       go(github.com/go-openapi/swag)
Requires:       go(github.com/google/btree)
Requires:       go(github.com/google/gnostic-models)
Requires:       go(github.com/google/gnostic-models/openapiv2)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/gorilla/websocket)
Requires:       go(github.com/josharian/intern)
Requires:       go(github.com/json-iterator/go)
Requires:       go(github.com/mailru/easyjson)
Requires:       go(github.com/moby/spdystream)
Requires:       go(github.com/modern-go/concurrent)
Requires:       go(github.com/modern-go/reflect2)
Requires:       go(github.com/munnerz/goautoneg)
Requires:       go(github.com/mxk/go-flowrate)
Requires:       go(github.com/peterbourgon/diskv)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/spf13/pflag)
Requires:       go(github.com/x448/float16)
Requires:       go(go.yaml.in/yaml/v2)
Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/net/http2)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/term)
Requires:       go(golang.org/x/text)
Requires:       go(golang.org/x/time)
Requires:       go(golang.org/x/time/rate)
Requires:       go(google.golang.org/protobuf)
Requires:       go(google.golang.org/protobuf/proto)
Requires:       go(gopkg.in/evanphx/json-patch.v4)
Requires:       go(gopkg.in/inf.v0)
Requires:       go(gopkg.in/yaml.v3)
Requires:       go(k8s.io/api)
Requires:       go(k8s.io/api/admissionregistration/v1)
Requires:       go(k8s.io/api/admissionregistration/v1alpha1)
Requires:       go(k8s.io/api/admissionregistration/v1beta1)
Requires:       go(k8s.io/api/apidiscovery/v2)
Requires:       go(k8s.io/api/apidiscovery/v2beta1)
Requires:       go(k8s.io/api/apiserverinternal/v1alpha1)
Requires:       go(k8s.io/api/apps/v1)
Requires:       go(k8s.io/api/apps/v1beta1)
Requires:       go(k8s.io/api/apps/v1beta2)
Requires:       go(k8s.io/api/authentication/v1)
Requires:       go(k8s.io/api/authentication/v1alpha1)
Requires:       go(k8s.io/api/authentication/v1beta1)
Requires:       go(k8s.io/api/authorization/v1)
Requires:       go(k8s.io/api/authorization/v1beta1)
Requires:       go(k8s.io/api/autoscaling/v1)
Requires:       go(k8s.io/api/autoscaling/v2)
Requires:       go(k8s.io/api/batch/v1)
Requires:       go(k8s.io/api/batch/v1beta1)
Requires:       go(k8s.io/api/certificates/v1)
Requires:       go(k8s.io/api/certificates/v1alpha1)
Requires:       go(k8s.io/api/certificates/v1beta1)
Requires:       go(k8s.io/api/coordination/v1)
Requires:       go(k8s.io/api/coordination/v1alpha2)
Requires:       go(k8s.io/api/coordination/v1beta1)
Requires:       go(k8s.io/api/core/v1)
Requires:       go(k8s.io/api/discovery/v1)
Requires:       go(k8s.io/api/discovery/v1beta1)
Requires:       go(k8s.io/api/events/v1)
Requires:       go(k8s.io/api/events/v1beta1)
Requires:       go(k8s.io/api/extensions/v1beta1)
Requires:       go(k8s.io/api/flowcontrol/v1)
Requires:       go(k8s.io/api/flowcontrol/v1beta1)
Requires:       go(k8s.io/api/flowcontrol/v1beta2)
Requires:       go(k8s.io/api/flowcontrol/v1beta3)
Requires:       go(k8s.io/api/imagepolicy/v1alpha1)
Requires:       go(k8s.io/api/networking/v1)
Requires:       go(k8s.io/api/networking/v1beta1)
Requires:       go(k8s.io/api/node/v1)
Requires:       go(k8s.io/api/node/v1alpha1)
Requires:       go(k8s.io/api/node/v1beta1)
Requires:       go(k8s.io/api/policy/v1)
Requires:       go(k8s.io/api/policy/v1beta1)
Requires:       go(k8s.io/api/rbac/v1)
Requires:       go(k8s.io/api/rbac/v1alpha1)
Requires:       go(k8s.io/api/rbac/v1beta1)
Requires:       go(k8s.io/api/resource/v1)
Requires:       go(k8s.io/api/resource/v1alpha3)
Requires:       go(k8s.io/api/resource/v1beta1)
Requires:       go(k8s.io/api/resource/v1beta2)
Requires:       go(k8s.io/api/scheduling/v1)
Requires:       go(k8s.io/api/scheduling/v1alpha1)
Requires:       go(k8s.io/api/scheduling/v1beta1)
Requires:       go(k8s.io/api/storage/v1)
Requires:       go(k8s.io/api/storage/v1alpha1)
Requires:       go(k8s.io/api/storage/v1beta1)
Requires:       go(k8s.io/api/storagemigration/v1beta1)
Requires:       go(k8s.io/apimachinery)
Requires:       go(k8s.io/apimachinery/pkg/api/errors)
Requires:       go(k8s.io/apimachinery/pkg/api/meta)
Requires:       go(k8s.io/apimachinery/pkg/api/meta/testrestmapper)
Requires:       go(k8s.io/apimachinery/pkg/api/resource)
Requires:       go(k8s.io/apimachinery/pkg/api/validation)
Requires:       go(k8s.io/apimachinery/pkg/apis/meta/internalversion)
Requires:       go(k8s.io/apimachinery/pkg/apis/meta/internalversion/scheme)
Requires:       go(k8s.io/apimachinery/pkg/apis/meta/internalversion/validation)
Requires:       go(k8s.io/apimachinery/pkg/apis/meta/v1)
Requires:       go(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured)
Requires:       go(k8s.io/apimachinery/pkg/apis/meta/v1beta1)
Requires:       go(k8s.io/apimachinery/pkg/conversion)
Requires:       go(k8s.io/apimachinery/pkg/fields)
Requires:       go(k8s.io/apimachinery/pkg/labels)
Requires:       go(k8s.io/apimachinery/pkg/runtime)
Requires:       go(k8s.io/apimachinery/pkg/runtime/schema)
Requires:       go(k8s.io/apimachinery/pkg/runtime/serializer)
Requires:       go(k8s.io/apimachinery/pkg/runtime/serializer/cbor)
Requires:       go(k8s.io/apimachinery/pkg/runtime/serializer/cbor/direct)
Requires:       go(k8s.io/apimachinery/pkg/runtime/serializer/json)
Requires:       go(k8s.io/apimachinery/pkg/runtime/serializer/streaming)
Requires:       go(k8s.io/apimachinery/pkg/runtime/serializer/versioning)
Requires:       go(k8s.io/apimachinery/pkg/types)
Requires:       go(k8s.io/apimachinery/pkg/util/cache)
Requires:       go(k8s.io/apimachinery/pkg/util/diff)
Requires:       go(k8s.io/apimachinery/pkg/util/errors)
Requires:       go(k8s.io/apimachinery/pkg/util/httpstream)
Requires:       go(k8s.io/apimachinery/pkg/util/httpstream/spdy)
Requires:       go(k8s.io/apimachinery/pkg/util/httpstream/wsstream)
Requires:       go(k8s.io/apimachinery/pkg/util/intstr)
Requires:       go(k8s.io/apimachinery/pkg/util/json)
Requires:       go(k8s.io/apimachinery/pkg/util/managedfields)
Requires:       go(k8s.io/apimachinery/pkg/util/naming)
Requires:       go(k8s.io/apimachinery/pkg/util/net)
Requires:       go(k8s.io/apimachinery/pkg/util/portforward)
Requires:       go(k8s.io/apimachinery/pkg/util/remotecommand)
Requires:       go(k8s.io/apimachinery/pkg/util/runtime)
Requires:       go(k8s.io/apimachinery/pkg/util/sets)
Requires:       go(k8s.io/apimachinery/pkg/util/strategicpatch)
Requires:       go(k8s.io/apimachinery/pkg/util/validation)
Requires:       go(k8s.io/apimachinery/pkg/util/version)
Requires:       go(k8s.io/apimachinery/pkg/util/wait)
Requires:       go(k8s.io/apimachinery/pkg/version)
Requires:       go(k8s.io/apimachinery/pkg/watch)
Requires:       go(k8s.io/klog/v2)
Requires:       go(k8s.io/kube-openapi)
Requires:       go(k8s.io/kube-openapi/pkg/handler3)
Requires:       go(k8s.io/kube-openapi/pkg/spec3)
Requires:       go(k8s.io/kube-openapi/pkg/util/proto)
Requires:       go(k8s.io/kube-openapi/pkg/validation/spec)
Requires:       go(k8s.io/utils)
Requires:       go(k8s.io/utils/buffer)
Requires:       go(k8s.io/utils/clock)
Requires:       go(k8s.io/utils/dump)
Requires:       go(k8s.io/utils/lru)
Requires:       go(k8s.io/utils/net)
Requires:       go(k8s.io/utils/ptr)
Requires:       go(k8s.io/utils/trace)
Requires:       go(sigs.k8s.io/json)
Requires:       go(sigs.k8s.io/randfill)
Requires:       go(sigs.k8s.io/structured-merge-diff/v6)
Requires:       go(sigs.k8s.io/structured-merge-diff/v6/fieldpath)
Requires:       go(sigs.k8s.io/structured-merge-diff/v6/typed)
Requires:       go(sigs.k8s.io/yaml)


%description
| ⚠️ **This is an automatically published **staged repository
 | (https://git.k8s.io/kubernetes/staging#external-repository-staging-
 | area)**
 | for Kubernetes**. Contributions, including issues and pull requests,
 | should be made to the main Kubernetes repository:
 | https://github.com/kubernetes/kubernetes
 | (https://github.com/kubernetes/kubernetes). This repository is read-
 | only
 | for importing, and not used for direct contributions. See
 | CONTRIBUTING.md (/CONTRIBUTING.md) for more details.


%files
%doc README.md
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
