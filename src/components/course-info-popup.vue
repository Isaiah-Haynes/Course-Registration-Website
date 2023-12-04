<template>
    <div class="admin__popup">
        <div class="admin__popup-inner">
            <slot />
            <button class="popup-close" @click="TogglePopup()">Close</button>
        </div>
    </div>
</template>

<script>
export default {
    props: ['TogglePopup']
}
</script>
<style lang="scss" scoped>
.admin__popup {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 99;
    background-color: rgba(0,0,0,0.2);
    display: flex;
    align-items: center;
    justify-content: center;

    .admin__popup-inner {
        background: #FFF;
        padding: 32px;
        
    }
    .popup-close {
        background: #3e71dc;
        width: 9rem;
        height: 2rem;
        padding: 0.8rem;
        border-radius: .5rem;
        -webkit-text-fill-color: #fafcff;
        font-size: 1.2rem;
        display: flex;
        align-items: center;
        justify-content: center;
}
}
</style>